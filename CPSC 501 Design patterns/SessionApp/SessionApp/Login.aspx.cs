using SessionApp.Utils;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace SessionApp
{
    public partial class Login : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void btnLogin_Click(object sender, EventArgs e)
        {
            Session.Timeout = 1; //in min
            string uname = txtUserName.Text;
            string password = txtPassw.Text;

            //go to db to verify a valid user
            if ((uname == "bill") && (password == "bill100")){
                lblStatus.Text = "welcome " + uname;
                //create session only if its a successful login
                //Session["LOGGEDIN"] = uname;
                SessionFacade.LOGGEDIN = uname;
            }

            else
            {
                lblStatus.Text = "Invalid Login";
            }
        }
    }
}