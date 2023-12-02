using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static Generics.MyEnums;

namespace Generics
{
    internal class StudentComparer : IComparer<Student>
    {
        SORTFIELD sortField = SORTFIELD.ID;
        public SORTFIELD SortField
        {
            get { return sortField; }
            set { sortField = value; }
        }
        SORTDIR sortDir = SORTDIR.ASC;
        public SORTDIR SortDir
        {
            get { return sortDir; }
            set { sortDir = value; }
        }
        #region IComparer<Student> Members
        public int Compare(Student x, Student y)
        {
            int res = x.CompareTo(y, sortField);
            if (sortDir == SORTDIR.DESC)
                res = -1 * res;
            return res;
        }
    }
    #endregion
}