$("#addToOrderBtn").on("click", function () {
  var _qty = $("#productQty").val();
  var _productId = $(".product-id").val();
  var _productTitle = $(".product-title").val();
  console.log(_qty, _productId, _productTitle);
});
