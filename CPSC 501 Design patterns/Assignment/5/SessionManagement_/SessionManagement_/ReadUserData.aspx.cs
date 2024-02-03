using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace SessionManagement_
{
    public partial class ReadUserData : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            //reading session data by casting
            lblUserData.Text = ((int)Session["UserData"]).ToString();
        }
    }
}