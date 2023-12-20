using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace SessionManagement_
{
    class MySingleton3
    {
        // readonly allows thread-safety
        // static members are lazily initialized.
        // static keyword makes the assignment to be only during declaration or within a constructor
        static readonly MySingleton3 instance = new MySingleton3();  

        MySingleton3() { }
        public static MySingleton3 Instance
        {
            get
            {
                return instance;
            }
        }
    }
}