using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace SessionManagement_
{
    class MySingleton //A private class,  not the best approach
    {
        static MySingleton instance = null;
        MySingleton() { } // private constructor
        public static MySingleton Instance
        {
            get
            {
                if (instance == null)
                    instance = new MySingleton();
                return instance;
            }
        }

    }
}