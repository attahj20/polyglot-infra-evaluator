const EventEmitter = require('events');
const metricsStream = new EventEmitter();

class RealTimeDashboardComponent {
    constructor(tenantId) {
        self.tenantId = tenantId;
    }

    mount() {
        // Production Flaw: Subscribing with an anonymous listener function without a teardown unbind strategy.
        // Every time this dashboard remounts or switches tenants, a new closure is allocated on metricsStream,
        // completely blocking older dashboard components from being garbage collected.
        metricsStream.on('metric_packet', (data) => {
            if (data.tenantId === self.tenantId) {
                console.log('Rendering telemetry packet:', data);
            }
        });
    }

    unmount() {
        console.log('Dashboard unmounted.');
    }
}
