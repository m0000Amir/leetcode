module.exports.parse = parse;

function parse(fetcher, src, chunkSize) {
  let data = [];
  let isFetched = false;

  async function fetchData() {
    const fetched = await fetcher(src);

    const _getData = (items) => {
      let res = [];

      for (let item of items) {
        if (!item.children) {
          res.push(item);
        } else {
          res.push({ type: item.type, value: item.value });
          res.push(..._getData(item.children));
        }
      }

      return res;
    };

    data = _getData(fetched);
    isFetched = true;
  }

  async function* getNextChunk() {
    if (!isFetched) {
      await fetchData();
    }

    let currentChunk = [];

    for (let item of data) {
      if (currentChunk.length >= chunkSize) {
        yield currentChunk.slice(0, chunkSize);
        currentChunk = currentChunk.slice(chunkSize);
      }

      if (item.type === 'data') {
        currentChunk.push(item.value);
      } else {
        for await (let chunk of parse(fetcher, item.src, chunkSize)) {
          currentChunk.push(...chunk);

          if (currentChunk.length >= chunkSize) {
            yield currentChunk.slice(0, chunkSize);
            currentChunk = currentChunk.slice(chunkSize);
          }
        }
      }
    }

    if (currentChunk.length) {
      yield currentChunk;
    }

    return;
  }

  return getNextChunk();
}
