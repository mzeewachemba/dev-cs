using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AbstractFactoryPattern
{
    //to allow different kinds of implementations eg. for different countries
    //different classes will produce different implementations of this interface 
    internal interface ICreditCheck
    {
        int GetCreditScore(string firstName, string lastName);
    }
}
