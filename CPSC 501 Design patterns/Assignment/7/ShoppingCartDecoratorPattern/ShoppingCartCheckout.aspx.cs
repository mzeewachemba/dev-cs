using ShoppingCartDecoratorPattern.Models;
using System;
using System.Collections.Generic;
using System.EnterpriseServices;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace ShoppingCartDecoratorPattern
{
    public partial class ShoppingCartCheckout : System.Web.UI.Page
    {
        //list of carts
        List<CartRow> CartList = new List<CartRow>();
        
        protected void Page_Load(object sender, EventArgs e)
        {
            
        }

        protected void btnCheckout_Click(object sender, EventArgs e)
        {
            //creating products and adding them into a cart
            CartRow row1 = new CartRow()
            {
                ProductId = 1001,
                ProductName = "Laptop",
                Price = 799.95m,
                Quantity = int.Parse(txtQt1.Text)
            };
            CartList.Add(row1);
            CartRow row2 = new CartRow()
            {
                ProductId = 1002,
                ProductName = "Camera",
                Price = 89.95m,
                Quantity = int.Parse(txtQt2.Text)
            };
            CartList.Add(row2);
            CartRow row3 = new CartRow()
            {
                ProductId = 1003,
                ProductName = "Calculator",
                Price = 39.90m,
                Quantity = int.Parse(txtQt3.Text)
            };
            CartList.Add(row3);
            //using the concrete class to calculate total before discount
            IShoppingCart cart = new ShoppingCart(); 
            cart.CartList = CartList;
            //modifying prices
            lblTotal1.Text = (int.Parse(txtQt1.Text) * 799.95).ToString();
            lblTotal2.Text = (int.Parse(txtQt2.Text) * 89.95).ToString();
            lblTotal3.Text = (int.Parse(txtQt3.Text) * 39.90).ToString();


            //calling on decorators by combining them together-chain of decorators
            //var decorator = new ShoppingCartHolidaySaleDecorator(new ShoppingCartFirstTimeCustomerDecorator(new ShoppingCartGT500Decorator(cart)));
            
            //applying holiday and GT500 Decorators
            var decorator = new ShoppingCartHolidaySaleDecorator(new ShoppingCartGT500Decorator(cart));

            //applying new customer Decorator
            //var decorator = new ShoppingCartFirstTimeCustomerDecorator(cart);
            var gtotal = decorator.ComputeTotal();
            lblMessage.Text = "Total before discount = " + cart.ComputeTotal().ToString() + "<br/>" +
            "After discounts = " + gtotal.ToString();
        }
    }
}