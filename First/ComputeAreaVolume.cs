using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace First
{
    internal class ComputeAreaVolume
    {
        //int width ;
        //public int Width
        //{
        //    get { return width; }
      
        //    set {
        //        if (width != value)
        //            throw new Exception("Width cannot be negative");
        //            width = value;
        //    }
        //}

        //int height;

        //public int Height
        //{
        //    get { return height; }

        //    set { height = value; }
        //}

        public int Width { get; set; }

        public int Height { get; set; }

        public double ComputeArea()
        {
            return Width * Height;
        }
    }
}
