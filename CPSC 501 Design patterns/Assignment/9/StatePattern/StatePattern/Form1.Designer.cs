namespace StatePattern
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
            btnTestStatePattern = new Button();
            SuspendLayout();
            // 
            // btnTestStatePattern
            // 
            btnTestStatePattern.Location = new Point(43, 31);
            btnTestStatePattern.Name = "btnTestStatePattern";
            btnTestStatePattern.Size = new Size(172, 36);
            btnTestStatePattern.TabIndex = 0;
            btnTestStatePattern.Text = "Test State Pattern";
            btnTestStatePattern.UseVisualStyleBackColor = true;
            btnTestStatePattern.Click += btnTestStatePattern_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(269, 366);
            Controls.Add(btnTestStatePattern);
            Name = "Form1";
            Text = "State";
            ResumeLayout(false);
        }

        #endregion

        private Button btnTestStatePattern;
    }
}
