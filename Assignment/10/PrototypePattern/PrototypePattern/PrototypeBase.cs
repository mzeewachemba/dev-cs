using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization.Formatters.Binary;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

namespace PrototypePattern
{
    [Serializable]
    abstract class ProtoTypeBase<T>
    {
        //this function creates a newly created copy of the object
        public T Copy()
        {
            MemoryStream mstr = new MemoryStream();
            //binary formatter got  deprecated vist here for alternatives https://learn.microsoft.com/en-us/dotnet/fundamentals/syslib-diagnostics/syslib0011
            // Disable the warning.
            #pragma warning disable SYSLIB0011
            BinaryFormatter bf = new BinaryFormatter();
            // Re-enable the warning.
            #pragma warning restore SYSLIB0011
            bf.Serialize(mstr, this);
            mstr.Seek(0, SeekOrigin.Begin);
            T cp = (T)bf.Deserialize(mstr);
            return cp;
        }
    }
}
