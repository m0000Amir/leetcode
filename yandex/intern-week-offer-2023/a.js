function a(orders){
  orders = orders.sort((a, b) => {
    if (a.expiredAt > b.expiredAt) {
      return 1;
    } else if (a.expiredAt === b.expiredAt) {
      return a.executionTime - b.executionTime;
    }
    return -1;
  });

  const dp = (currentTime, currentOrders) => {
    if (!currentOrders || currentOrders.length === 0) return 0;

    const cur = currentOrders[0];

    if (currentTime + cur.executionTime > cur.expiredAt) {
      return dp(currentTime, currentOrders.slice(1));
    } else {
      return Math.max(
        dp(currentTime, currentOrders.slice(1)),
        1 + dp(currentTime + cur.executionTime, currentOrders.slice(1)),
      );
    }
  };

  return dp(0, orders);
}


const orders = [{"index":"0000","executionTime":100,"expiredAt":200},{"index":"0001","executionTime":1000,"expiredAt":1250},{"index":"0002","executionTime":200,"expiredAt":1300},{"index":"0003","executionTime":2000,"expiredAt":3200}];


console.log(a(orders));
