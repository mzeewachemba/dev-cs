﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TemplatePattern
{
    abstract class TemplateStudent //base to define steps for an algorithms
    {
        protected List<Student> _STList = new List<Student>();
        public List<Student> STList
        {
            get { return _STList; }
            set { _STList = value; }
        }//below methods implementations to be done by child classes
        public abstract void ReadStudents();
        public abstract void AssignGrades();
        public abstract void SortStudents();
        public abstract void StoreStudents();

        // algorithm steps
        public void ReadAndProcessStudents()
        {
            ReadStudents(); // from XML or comma delimited file, or DB
            AssignGrades(); // Formula may change
            SortStudents(); // Sort by Quick or Shell Sort, any field
            StoreStudents(); // Emit tab delimited file or XML, or DB
        }
    }
}
