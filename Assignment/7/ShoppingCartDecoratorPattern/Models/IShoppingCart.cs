using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ShoppingCartDecoratorPattern.Models
{
    public interface IShoppingCart //base interface
    {
        List<CartRow> CartList { get; set; }
        decimal ComputeTotal();
    }
}
