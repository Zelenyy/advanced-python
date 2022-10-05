names=("2.7", "3.5", "3.6", "3.7", "3.8", "3.9", "3.10")



conda activate spc_py3.5
python --version
python mandelbrot.py
conda deactivate

#for ((i = 0; i < 7; i++))
#do
#  conda activate "spc_py${names[$i]}"
#  python --version
#  python mandelbrot.py
#  conda deactivate
#done