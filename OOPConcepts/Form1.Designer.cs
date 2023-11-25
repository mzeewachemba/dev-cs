namespace OOPConcepts
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
            btnGenClass = new Button();
            btnTestList = new Button();
            btnExtMethod = new Button();
            SuspendLayout();
            // 
            // btnExchange
            // 
            btnExchange.Location = new Point(47, 49);
            btnExchange.Name = "btnExchange";
            btnExchange.Size = new Size(94, 29);
            btnExchange.TabIndex = 0;
            btnExchange.Text = "Exchange Data";
            btnExchange.UseVisualStyleBackColor = true;
            btnExchange.Click += btnExchange_Click;
            // 
            // btnGenClass
            // 
            btnGenClass.Location = new Point(225, 49);
            btnGenClass.Name = "btnGenClass";
            btnGenClass.Size = new Size(94, 29);
            btnGenClass.TabIndex = 1;
            btnGenClass.Text = "Gen Class";
            btnGenClass.UseVisualStyleBackColor = true;
            btnGenClass.Click += btnGenClass_Click;
            // 
            // btnTestList
            // 
            btnTestList.Location = new Point(47, 138);
            btnTestList.Name = "btnTestList";
            btnTestList.Size = new Size(94, 29);
            btnTestList.TabIndex = 2;
            btnTestList.Text = "Test List";
            btnTestList.UseVisualStyleBackColor = true;
            btnTestList.Click += btnTestList_Click;
            // 
            // btnExtMethod
            // 
            btnExtMethod.Location = new Point(225, 138);
            btnExtMethod.Name = "btnExtMethod";
            btnExtMethod.Size = new Size(94, 29);
            btnExtMethod.TabIndex = 3;
            btnExtMethod.Text = "Extension Method";
            btnExtMethod.UseVisualStyleBackColor = true;
            btnExtMethod.Click += btnExtMethod_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(422, 362);
            Controls.Add(btnExtMethod);
            Controls.Add(btnTestList);
            Controls.Add(btnGenClass);
            Controls.Add(btnExchange);
            Name = "Form1";
            Text = "Form1";
            ResumeLayout(false);
        }

        #endregion

        private Button btnExchange;
        private Button btnGenClass;
        private Button btnTestList;
        private Button btnExtMethod;
    }
}