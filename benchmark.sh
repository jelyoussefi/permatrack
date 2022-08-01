cd /workspace/permatrack/src && \
mkdir -p ../data/output
python test.py tracking \
	--exp_id pd \
	--dataset pd_tracking \
	--dataset_version val \
	--track_thresh 0.4 \
	--load_model ../data/models/pd_17fr_21ep_vis.pth \
	--is_recurrent \
	--gru_filter_size 7 \
	--num_gru_layers 1 \
	--stream_test \
	--debug 4 \
	--debug_dir ../data/output
