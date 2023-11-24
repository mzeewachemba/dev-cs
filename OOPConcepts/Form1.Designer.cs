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
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(436, 223);
            Controls.Add(btnGenClass);
            Controls.Add(btnExchange);
            Name = "Form1";
            Text = "Form1";
            ResumeLayout(false);
        }

        #endregion

        private Button btnExchange;
        private Button btnGenClass;
    }
}