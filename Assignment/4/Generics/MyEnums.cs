using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Generics
{
    internal class MyEnums
    {
        public enum SORTFIELD : int
        {
            FIRSTNAME,
            LASTNAME,
            ID,
            TEST1SCORE,
            TEST2SCORE
        }
        public enum SORTDIR : int
        {
            ASC,
            DESC
        }

    }
}
