using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace ShoppingCartDecoratorPattern.Models
{
    //for 10% off of holiday sale
    public class ShoppingCartHolidaySaleDecorator : ShoppingCartBaseDecorator
    {// aggregation and a call base class construct[or
        public ShoppingCartHolidaySaleDecorator(IShoppingCart shoppingCart) : base(shoppingCart) 
        {
        }
        public override decimal ComputeTotal()
        { // 10% holiday sale
            decimal grandTotal = 0;
            grandTotal = _shoppingCart.ComputeTotal();
            grandTotal = grandTotal - (grandTotal * (decimal)(10 / 100.0));
            return grandTotal;
        }
    }
}