using SessionManagement_.Utils;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace SessionManagement_
{
    public partial class Login : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }
        protected void btnLogin_Click(object sender, EventArgs e)
        {
            if ((txtUsername.Text == "bill") && (txtPassword.Text == "bill100"))
            {
                lblStatus.Text = "Welcome " + txtUsername.Text + "..";
                //setting up some values
                SessionFacade.LastLogin = DateTime.Now;
                SessionFacade.UserName = txtUsername.Text;
                SessionFacade.Account = 1234;
            }
        }
    }
}