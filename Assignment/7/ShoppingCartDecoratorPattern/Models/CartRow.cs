using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace ShoppingCartDecoratorPattern.Models
{
    public class CartRow
    {
        public int ProductId { get; set; }
        public string ProductName { get; set; }
        public decimal Price { get; set; }
        public int Quantity { get; set; }
        public decimal PriceTotal { get; set; }

    }
}