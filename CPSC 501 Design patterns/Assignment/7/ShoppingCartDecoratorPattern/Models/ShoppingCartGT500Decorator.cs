using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace ShoppingCartDecoratorPattern.Models
{
    //decorator provides a discount of 5% if the purchase total is greater than 500 dollars
    public class ShoppingCartGT500Decorator : ShoppingCartBaseDecorator
    {
        public ShoppingCartGT500Decorator(IShoppingCart shoppingCart) : base(shoppingCart) // aggregation to base constructor
        {
        }
        public override decimal ComputeTotal()
        {
            decimal grandTotal = 0;
            grandTotal = _shoppingCart.ComputeTotal();
            if (grandTotal > 500)
            {
                grandTotal = grandTotal - (grandTotal * (decimal)(5 / 100.0));
            }
            return grandTotal;
        }
    }
}