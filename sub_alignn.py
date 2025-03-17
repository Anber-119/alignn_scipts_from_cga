#!/bin/bash
#SBATCH -n 80       # 单节点核数
#SBATCH -N 1        # 申请一台节点
#SBATCH --mail-type=ALL
#SBATCH --mail-user=<如需邮件提示功能，请在此填写自己的邮箱地址>

# 打印任务信息
echo "Starting job $SLURM_JOB_ID at " `date`
echo "SLURM_SUBMIT_DIR is $SLURM_SUBMIT_DIR"
echo "Running on nodes: $SLURM_NODELIST"

# 执行任务
## 载入虚拟环境
module load anaconda3
ulimit -s unlimited
train_alignn.py --root_dir "/home/yanli/abw/alignn-install/alignn/examples/sample_data/" --config "/home/yanli/abw/alignn-install/alignn/examples/sample_data/config_example.json" --output_dir=temp > alignn.log 2>&1

# 任务结束
echo "Job $SLURM_JOB_ID done at " `date`
