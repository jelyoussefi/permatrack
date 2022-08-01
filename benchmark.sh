cd /workspace/permatrack/src/lib/model/networks/DCNv2/ && ./make.sh 

cd /workspace/permatrack/src && \
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
	--not_show_bbox \
	--debug 5
