ARG SUMO_TAG=1.4.0
ARG NS3_TAG=3.33

FROM osmhpi/sumo:$SUMO_TAG AS sumo

FROM osmhpi/ns-3:$NS3_TAG

RUN pip3 install --no-cache-dir \
	coloredlogs \
	docker \
	nsenter \
	paramiko \
	pylxd \
	pyroute2 \
	pyyaml \
	git+https://github.com/active-expressions/active-expressions-static-python

# Copy the sumo python packages (traci, sumolib and libsumo) from the sumo image
COPY --from=sumo /usr/local/lib/python3.7 /usr/local/lib/python3.7

ENV COLOREDLOGS_DATE_FORMAT="%H:%M:%S" \
	COLOREDLOGS_LOG_FORMAT="%(asctime)s %(name)-32s %(levelname)-8s %(message)s" \
	COLOREDLOGS_LOG_LEVEL="DEBUG" \
	COLOREDLOGS_LEVEL_STYLES="debug=cyan;warning=yellow;error=red;critical=red,bold" \
	COLOREDLOGS_AUTO_INSTALL="true" \
	PYLXD_WARNINGS="none"
