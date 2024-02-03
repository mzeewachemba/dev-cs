namespace DecoratorPattern
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
            btnDecoratorSimple = new Button();
            btnSubClassing = new Button();
            SuspendLayout();
            // 
            // btnDecoratorSimple
            // 
            btnDecoratorSimple.Location = new Point(42, 34);
            btnDecoratorSimple.Name = "btnDecoratorSimple";
            btnDecoratorSimple.Size = new Size(181, 48);
            btnDecoratorSimple.TabIndex = 0;
            btnDecoratorSimple.Text = "Decorator Simple";
            btnDecoratorSimple.UseVisualStyleBackColor = true;
            btnDecoratorSimple.Click += btnDecoratorSimple_Click;
            // 
            // btnSubClassing
            // 
            btnSubClassing.Location = new Point(42, 151);
            btnSubClassing.Name = "btnSubClassing";
            btnSubClassing.Size = new Size(181, 52);
            btnSubClassing.TabIndex = 1;
            btnSubClassing.Text = "Sub Classing";
            btnSubClassing.UseVisualStyleBackColor = true;
            btnSubClassing.Click += btnSubClassing_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(288, 450);
            Controls.Add(btnSubClassing);
            Controls.Add(btnDecoratorSimple);
            Name = "Form1";
            Text = "Decorator Pattern";
            ResumeLayout(false);
        }

        #endregion

        private Button button1;
        private Button btnDecoratorSimple;
        private Button btnSubClassing;
    }
}
