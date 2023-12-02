namespace Generics
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            btnExchange = new Button();
            btnGenericClass = new Button();
            btnInitArray = new Button();
            btnFindMaxScoreStudent = new Button();
            btnComparerGeneric = new Button();
            btnDictionary = new Button();
            SuspendLayout();
            // 
            // btnExchange
            // 
            btnExchange.Location = new Point(45, 45);
            btnExchange.Name = "btnExchange";
            btnExchange.Size = new Size(226, 43);
            btnExchange.TabIndex = 0;
            btnExchange.Text = "Exchange";
            btnExchange.UseVisualStyleBackColor = true;
            btnExchange.Click += btnExchange_Click;
            // 
            // btnGenericClass
            // 
            btnGenericClass.Location = new Point(45, 109);
            btnGenericClass.Name = "btnGenericClass";
            btnGenericClass.Size = new Size(226, 44);
            btnGenericClass.TabIndex = 1;
            btnGenericClass.Text = "Generic Class";
            btnGenericClass.UseVisualStyleBackColor = true;
            btnGenericClass.Click += btnGenericClass_Click;
            // 
            // btnInitArray
            // 
            btnInitArray.Location = new Point(45, 187);
            btnInitArray.Name = "btnInitArray";
            btnInitArray.Size = new Size(226, 40);
            btnInitArray.TabIndex = 2;
            btnInitArray.Text = "Init Array";
            btnInitArray.UseVisualStyleBackColor = true;
            btnInitArray.Click += btnInitArray_Click;
            // 
            // btnFindMaxScoreStudent
            // 
            btnFindMaxScoreStudent.Location = new Point(45, 261);
            btnFindMaxScoreStudent.Name = "btnFindMaxScoreStudent";
            btnFindMaxScoreStudent.Size = new Size(226, 45);
            btnFindMaxScoreStudent.TabIndex = 3;
            btnFindMaxScoreStudent.Text = "Find Max Score Student";
            btnFindMaxScoreStudent.UseVisualStyleBackColor = true;
            btnFindMaxScoreStudent.Click += btnFindMaxScoreStudent_Click;
            // 
            // btnComparerGeneric
            // 
            btnComparerGeneric.Location = new Point(45, 337);
            btnComparerGeneric.Name = "btnComparerGeneric";
            btnComparerGeneric.Size = new Size(226, 49);
            btnComparerGeneric.TabIndex = 4;
            btnComparerGeneric.Text = "Comparer Generic";
            btnComparerGeneric.UseVisualStyleBackColor = true;
            btnComparerGeneric.Click += btnComparerGeneric_Click;
            // 
            // btnDictionary
            // 
            btnDictionary.Location = new Point(45, 409);
            btnDictionary.Name = "btnDictionary";
            btnDictionary.Size = new Size(226, 50);
            btnDictionary.TabIndex = 5;
            btnDictionary.Text = "Dictionary";
            btnDictionary.UseVisualStyleBackColor = true;
            btnDictionary.Click += btnDictionary_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 471);
            Controls.Add(btnDictionary);
            Controls.Add(btnComparerGeneric);
            Controls.Add(btnFindMaxScoreStudent);
            Controls.Add(btnInitArray);
            Controls.Add(btnGenericClass);
            Controls.Add(btnExchange);
            Name = "Form1";
            Text = "Generics Display";
            ResumeLayout(false);
        }

        #endregion

        private Button btnExchange;
        private Button btnGenericClass;
        private Button btnInitArray;
        private Button btnFindMaxScoreStudent;
        private Button btnComparerGeneric;
        private Button btnDictionary;
    }
}