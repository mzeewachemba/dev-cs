namespace AbstractFactoryPattern
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
            btnAbstractFactoryUS = new Button();
            btnAbstractFactoryCanada = new Button();
            SuspendLayout();
            // 
            // btnAbstractFactoryUS
            // 
            btnAbstractFactoryUS.Location = new Point(44, 46);
            btnAbstractFactoryUS.Name = "btnAbstractFactoryUS";
            btnAbstractFactoryUS.Size = new Size(244, 39);
            btnAbstractFactoryUS.TabIndex = 0;
            btnAbstractFactoryUS.Text = "Abstract Factory US";
            btnAbstractFactoryUS.UseVisualStyleBackColor = true;
            btnAbstractFactoryUS.Click += btnAbstractFactoryUS_Click;
            // 
            // btnAbstractFactoryCanada
            // 
            btnAbstractFactoryCanada.Location = new Point(44, 112);
            btnAbstractFactoryCanada.Name = "btnAbstractFactoryCanada";
            btnAbstractFactoryCanada.Size = new Size(244, 43);
            btnAbstractFactoryCanada.TabIndex = 1;
            btnAbstractFactoryCanada.Text = "Abstract Factory Canada";
            btnAbstractFactoryCanada.UseVisualStyleBackColor = true;
            btnAbstractFactoryCanada.Click += btnAbstractFactoryCanada_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(370, 279);
            Controls.Add(btnAbstractFactoryCanada);
            Controls.Add(btnAbstractFactoryUS);
            Name = "Form1";
            Text = "Abstract Factory";
            Load += Form1_Load;
            ResumeLayout(false);
        }

        #endregion

        private Button btnAbstractFactoryUS;
        private Button btnAbstractFactoryCanada;
    }
}
