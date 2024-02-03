namespace StudentApp
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
            btnTestStudent = new Button();
            btnTestGrad = new Button();
            btnPoly = new Button();
            SuspendLayout();
            // 
            // btnTestStudent
            // 
            btnTestStudent.Location = new Point(26, 39);
            btnTestStudent.Name = "btnTestStudent";
            btnTestStudent.Size = new Size(210, 52);
            btnTestStudent.TabIndex = 0;
            btnTestStudent.Text = "Test Student";
            btnTestStudent.UseVisualStyleBackColor = true;
            btnTestStudent.Click += btnTestStudent_Click;
            // 
            // btnTestGrad
            // 
            btnTestGrad.Location = new Point(26, 161);
            btnTestGrad.Name = "btnTestGrad";
            btnTestGrad.Size = new Size(210, 38);
            btnTestGrad.TabIndex = 1;
            btnTestGrad.Text = "Test Graduate Student";
            btnTestGrad.UseVisualStyleBackColor = true;
            btnTestGrad.Click += btnTestGrad_Click;
            // 
            // btnPoly
            // 
            btnPoly.Location = new Point(26, 267);
            btnPoly.Name = "btnPoly";
            btnPoly.Size = new Size(210, 38);
            btnPoly.TabIndex = 2;
            btnPoly.Text = "Test Poly";
            btnPoly.UseVisualStyleBackColor = true;
            btnPoly.Click += btnPoly_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(btnPoly);
            Controls.Add(btnTestGrad);
            Controls.Add(btnTestStudent);
            Name = "Form1";
            Text = "Form1";
            ResumeLayout(false);
        }

        #endregion

        private Button btnTestStudent;
        private Button btnTestGrad;
        private Button btnPoly;
    }
}