using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace ShoppingCartDecoratorPattern.Models
{
    public class ShoppingCart : IShoppingCart //base component concrete
    {
        public List<CartRow> CartList { get; set; } // list of items in cart
        public decimal ComputeTotal() //calculating total
        {
            decimal grandTotal = 0;
            foreach (CartRow row in CartList)
            {
                row.PriceTotal = row.Price * row.Quantity;
                grandTotal += row.PriceTotal;
            }
            return grandTotal;
        }
    }
}