using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace SessionTest
{
    public partial class Page2 : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void btnReadData_Click(object sender, EventArgs e)
        {
            int data = (int)Session["UserData"];
            lblUserData.Text = data.ToString();
        }
    }
}