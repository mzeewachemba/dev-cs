using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace SessionApp.Utils
{
    public class SessionFacade
    {
        const string LoggedIn = "LoggedIn"; //key, fixing the keyword
        public static string LOGGEDIN
        {
            get
            {
                if (HttpContext.Current.Session[LoggedIn] != null)
                    return (string)HttpContext.Current.Session[LoggedIn];
                else return null;
            }
            set
            {
                HttpContext.Current.Session[LoggedIn] = value;
            }
        }
    }
}