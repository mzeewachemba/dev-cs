namespace VisitorPattern
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
            btnVisitor = new Button();
            btnAddOverTime = new Button();
            btnAddComputePayMethod = new Button();
            btnOverTimeExtension = new Button();
            SuspendLayout();
            // 
            // btnVisitor
            // 
            btnVisitor.Location = new Point(57, 55);
            btnVisitor.Name = "btnVisitor";
            btnVisitor.Size = new Size(194, 47);
            btnVisitor.TabIndex = 0;
            btnVisitor.Text = "Visitor";
            btnVisitor.UseVisualStyleBackColor = true;
            btnVisitor.Click += btnVisitor_Click;
            // 
            // btnAddOverTime
            // 
            btnAddOverTime.Location = new Point(57, 251);
            btnAddOverTime.Name = "btnAddOverTime";
            btnAddOverTime.Size = new Size(194, 43);
            btnAddOverTime.TabIndex = 1;
            btnAddOverTime.Text = "Over Time";
            btnAddOverTime.UseVisualStyleBackColor = true;
            btnAddOverTime.Click += btnAddOverTime_Click;
            // 
            // btnAddComputePayMethod
            // 
            btnAddComputePayMethod.Location = new Point(57, 150);
            btnAddComputePayMethod.Name = "btnAddComputePayMethod";
            btnAddComputePayMethod.Size = new Size(194, 48);
            btnAddComputePayMethod.TabIndex = 2;
            btnAddComputePayMethod.Text = "Compute Pay Method";
            btnAddComputePayMethod.UseVisualStyleBackColor = true;
            btnAddComputePayMethod.Click += btnAddComputePayMethod_Click;
            // 
            // btnOverTimeExtension
            // 
            btnOverTimeExtension.Location = new Point(57, 340);
            btnOverTimeExtension.Name = "btnOverTimeExtension";
            btnOverTimeExtension.Size = new Size(194, 43);
            btnOverTimeExtension.TabIndex = 3;
            btnOverTimeExtension.Text = "Over Time Extension";
            btnOverTimeExtension.UseVisualStyleBackColor = true;
            btnOverTimeExtension.Click += btnOverTimeExtension_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(320, 450);
            Controls.Add(btnOverTimeExtension);
            Controls.Add(btnAddComputePayMethod);
            Controls.Add(btnAddOverTime);
            Controls.Add(btnVisitor);
            Name = "Form1";
            Text = "Visitor";
            ResumeLayout(false);
        }

        #endregion

        private Button btnVisitor;
        private Button btnAddOverTime;
        private Button btnAddComputePayMethod;
        private Button btnOverTimeExtension;
    }
}
