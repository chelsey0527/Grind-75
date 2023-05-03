/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
  let maxProfit = 0;

  for ( let i = 0; i < prices.length; i++){
      for ( let j = prices.length-1; j > i; j--){
          if ( prices[j] - prices[i] > maxProfit ){
              maxProfit = prices[j] - prices[i];
          }
      }
  }

  return maxProfit;
  
};