namespace FactoryPattern
{
    partial class fmWeather
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
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
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.btnWeatherFactory = new System.Windows.Forms.Button();
            this.btnComputeFactory = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // btnWeatherFactory
            // 
            this.btnWeatherFactory.Location = new System.Drawing.Point(46, 50);
            this.btnWeatherFactory.Name = "btnWeatherFactory";
            this.btnWeatherFactory.Size = new System.Drawing.Size(215, 44);
            this.btnWeatherFactory.TabIndex = 0;
            this.btnWeatherFactory.Text = "Weather Factory";
            this.btnWeatherFactory.UseVisualStyleBackColor = true;
            this.btnWeatherFactory.Click += new System.EventHandler(this.btnWeatherFactory_Click);
            // 
            // btnComputeFactory
            // 
            this.btnComputeFactory.Location = new System.Drawing.Point(46, 143);
            this.btnComputeFactory.Name = "btnComputeFactory";
            this.btnComputeFactory.Size = new System.Drawing.Size(215, 38);
            this.btnComputeFactory.TabIndex = 1;
            this.btnComputeFactory.Text = "Compute Factory";
            this.btnComputeFactory.UseVisualStyleBackColor = true;
            this.btnComputeFactory.Click += new System.EventHandler(this.btnComputeFactory_Click);
            // 
            // fmWeather
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(329, 349);
            this.Controls.Add(this.btnComputeFactory);
            this.Controls.Add(this.btnWeatherFactory);
            this.Name = "fmWeather";
            this.Text = "Weather";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btnWeatherFactory;
        private System.Windows.Forms.Button btnComputeFactory;
    }
}

