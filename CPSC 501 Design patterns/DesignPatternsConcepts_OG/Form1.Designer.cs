namespace DesignPatternsConcepts
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
            btnTest = new Button();
            btnTestFactory = new Button();
            SuspendLayout();
            // 
            // btnTest
            // 
            btnTest.Location = new Point(58, 56);
            btnTest.Name = "btnTest";
            btnTest.Size = new Size(244, 55);
            btnTest.TabIndex = 0;
            btnTest.Text = "Test";
            btnTest.UseVisualStyleBackColor = true;
            btnTest.Click += btnTest_Click;
            // 
            // btnTestFactory
            // 
            btnTestFactory.Location = new Point(58, 158);
            btnTestFactory.Name = "btnTestFactory";
            btnTestFactory.Size = new Size(244, 49);
            btnTestFactory.TabIndex = 1;
            btnTestFactory.Text = "Test Factory";
            btnTestFactory.UseVisualStyleBackColor = true;
            btnTestFactory.Click += btnTestFactory_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(btnTestFactory);
            Controls.Add(btnTest);
            Name = "Form1";
            Text = "Test";
            ResumeLayout(false);
        }

        #endregion

        private Button btnTest;
        private Button btnTestFactory;
    }
}