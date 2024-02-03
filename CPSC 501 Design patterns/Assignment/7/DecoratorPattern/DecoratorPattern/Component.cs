using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DecoratorPattern
{
    //concrete implementation of a class
    internal class Component : IComponent
    {
        public virtual string Welcome()
        {
            return "Welcome to our group";
        }
        public virtual string Welcome(string name)
        {
            return name + " Welcome to our group";
        }
    }
}
