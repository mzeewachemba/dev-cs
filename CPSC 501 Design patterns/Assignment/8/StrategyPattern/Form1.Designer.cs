namespace StrategyPattern
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
            btnStrategySort = new Button();
            btnStrategySortUniversity = new Button();
            SuspendLayout();
            // 
            // btnStrategySort
            // 
            btnStrategySort.Location = new Point(47, 40);
            btnStrategySort.Name = "btnStrategySort";
            btnStrategySort.Size = new Size(152, 40);
            btnStrategySort.TabIndex = 0;
            btnStrategySort.Text = "Strategy Sort";
            btnStrategySort.UseVisualStyleBackColor = true;
            btnStrategySort.Click += btnStrategySort_Click;
            // 
            // btnStrategySortUniversity
            // 
            btnStrategySortUniversity.Location = new Point(47, 128);
            btnStrategySortUniversity.Name = "btnStrategySortUniversity";
            btnStrategySortUniversity.Size = new Size(197, 43);
            btnStrategySortUniversity.TabIndex = 1;
            btnStrategySortUniversity.Text = "Strategy Sort University";
            btnStrategySortUniversity.UseVisualStyleBackColor = true;
            btnStrategySortUniversity.Click += btnStrategySortUniversity_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(314, 231);
            Controls.Add(btnStrategySortUniversity);
            Controls.Add(btnStrategySort);
            Name = "Form1";
            Text = "Strategy";
            ResumeLayout(false);
        }

        #endregion

        private Button btnStrategySort;
        private Button btnStrategySortUniversity;
    }
}
