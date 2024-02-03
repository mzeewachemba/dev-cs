using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace SessionManagement_
{
    public partial class Page1 : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            //storing session data
            Session["Userdata"] = 25;
            Response.Write("User data set to " + ((int)(Session["Userdata"])).ToString());
        }
    }
}