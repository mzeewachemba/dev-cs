using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace SessionManagement_.Utils
{
    public class SessionFacade
    {
        SessionFacade()
        {
        }
        // these values wont change for the key names, error proof
        const string USERNAME = "USERNAME";
        const string ACCOUNTNUM = "ACCOUNTNUM"; // integer storage
        const string LASTLOGIN = "LASTLOGIN"; // datetime
        
        //properties for session data Username, Account, Last Login
        public static string UserName
        {
            get
            {
                if (HttpContext.Current.Session[USERNAME] != null)
                    return (string)HttpContext.Current.Session[USERNAME];
                else
                    return null;
            }
            set
            {
                HttpContext.Current.Session[USERNAME] = value;
            }
        }
        public static int? Account
        {
            get
            {
                if (HttpContext.Current.Session[ACCOUNTNUM] != null)
                    return (int)HttpContext.Current.Session[ACCOUNTNUM];
                else
                    return null;
            }
            set
            {
                HttpContext.Current.Session[ACCOUNTNUM] = value;
            }
        }
        public static DateTime LastLogin
        {
            get
            {
                if (HttpContext.Current.Session[LASTLOGIN] != null)
                    return (DateTime)HttpContext.Current.Session[LASTLOGIN];
                else
                    return DateTime.MinValue; // or use nullable
            }
            set
            {
                HttpContext.Current.Session[LASTLOGIN] = value;
            }
        }
    }
}