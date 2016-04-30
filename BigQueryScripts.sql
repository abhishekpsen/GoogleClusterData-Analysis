-- Remove events
SELECT integer(round(timestamp/(86400000000),0)) as time_minute, count(1) as remove_events FROM [google_cloud_data.machine_events]
where event_type = 1
group by time_minute
order by time_minute

-- Add events
SELECT integer(round(timestamp/(86400000000),0)) as time_minute, count(1) as add_events FROM [google_cloud_data.machine_events]
where event_type = 0
group by time_minute
order by time_minute

-- Update events
SELECT integer(round(timestamp/(86400000000),0)) as time_minute, count(1) as update_events FROM [google_cloud_data.machine_events]
where event_type = 2
group by time_minute
order by time_minute

-- Get failure counts by platform id
SELECT platform_id, count(1) as failures FROM [google_cloud_data.machine_events]
where event_type = 1
group by platform_id

-- Get update counts by platform id
SELECT platform_id, count(1) as updates FROM [google_cloud_data.machine_events]
where event_type = 2
group by platform_id
