using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StrategyPattern
{
    internal class University //maintains a list of student
    {
        private IStrategySort<Student> _sortStrategy;
        internal IStrategySort<Student> SortStrategy
        {
            get { return _sortStrategy; }
            set { _sortStrategy = value; }
        }
        public University(IStrategySort<Student> sortStrategy)
        {
            this._sortStrategy = sortStrategy;
        }
        private List<Student> _STList = new List<Student>();
        public List<Student> STList
        {
            get { return _STList; }
            set { _STList = value; }
        }
        public void AddStudent(Student st)
        {
            _STList.Add(st);
        }
        public void SortStudent()
        {
            _sortStrategy.DoSort(STList); // will sort via Shell or QuickSort
        }
    }
}
