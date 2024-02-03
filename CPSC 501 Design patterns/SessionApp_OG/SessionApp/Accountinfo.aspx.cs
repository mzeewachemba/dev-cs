using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace SessionApp
{
    public partial class Accountinfo : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            if (Session["LOGGEDIN"] == null)
            {
                Response.Redirect("Login.aspx");
            }
            //go to db and obtain account balance
            txtName.Text = "Bill Baker";
            txtBalance.Text = "9878098.8987";
            lblSessioninfo.Text = Session.SessionID;
        }
    }
}