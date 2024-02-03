using SessionManagement_.Utils;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace SessionManagement_
{
    public partial class Status : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            try
            {
                lblUsername.Text = SessionFacade.UserName;
                lblAccountNum.Text = SessionFacade.Account.ToString();
                lblLastLogin.Text = SessionFacade.LastLogin.ToString();
            }
            catch (Exception ex)
            {
                lblStatus.Text = ex.Message;
            }
        }
    }
}