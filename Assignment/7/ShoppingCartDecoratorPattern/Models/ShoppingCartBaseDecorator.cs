using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace ShoppingCartDecoratorPattern.Models
{
    public abstract class ShoppingCartBaseDecorator : IShoppingCart //decorators base class
    {
        public List<CartRow> CartList { get; set; }
        public decimal OriginalGrandTotal { get; set; } // before discounts
        protected IShoppingCart _shoppingCart;
        public ShoppingCartBaseDecorator(IShoppingCart shoppingCart)
        {
            _shoppingCart = shoppingCart;
        }
        public abstract decimal ComputeTotal();
    }
}