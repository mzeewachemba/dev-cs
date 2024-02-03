namespace TemplatePattern
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
            btnTemplate = new Button();
            btnTemplateStrategy = new Button();
            btnTemplateStrategyDB = new Button();
            SuspendLayout();
            // 
            // btnTemplate
            // 
            btnTemplate.Location = new Point(42, 28);
            btnTemplate.Name = "btnTemplate";
            btnTemplate.Size = new Size(177, 38);
            btnTemplate.TabIndex = 0;
            btnTemplate.Text = "Template";
            btnTemplate.UseVisualStyleBackColor = true;
            btnTemplate.Click += btnTemplate_Click;
            // 
            // btnTemplateStrategy
            // 
            btnTemplateStrategy.Location = new Point(42, 153);
            btnTemplateStrategy.Name = "btnTemplateStrategy";
            btnTemplateStrategy.Size = new Size(177, 44);
            btnTemplateStrategy.TabIndex = 1;
            btnTemplateStrategy.Text = "Template Strategy File";
            btnTemplateStrategy.UseVisualStyleBackColor = true;
            btnTemplateStrategy.Click += btnTemplateStrategy_Click;
            // 
            // btnTemplateStrategyDB
            // 
            btnTemplateStrategyDB.Location = new Point(42, 253);
            btnTemplateStrategyDB.Name = "btnTemplateStrategyDB";
            btnTemplateStrategyDB.Size = new Size(177, 44);
            btnTemplateStrategyDB.TabIndex = 2;
            btnTemplateStrategyDB.Text = "Template Strategy DB";
            btnTemplateStrategyDB.UseVisualStyleBackColor = true;
            btnTemplateStrategyDB.Click += btnTemplateStrategyDB_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(302, 450);
            Controls.Add(btnTemplateStrategyDB);
            Controls.Add(btnTemplateStrategy);
            Controls.Add(btnTemplate);
            Name = "Form1";
            Text = "Template";
            ResumeLayout(false);
        }

        #endregion

        private Button btnTemplate;
        private Button btnTemplateStrategy;
        private Button btnTemplateStrategyDB;
    }
}
