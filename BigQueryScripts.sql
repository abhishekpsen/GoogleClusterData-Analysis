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


--Jobs scheduled and then failed, killed or lost
select job_id, count(job_id) from [google_cloud_data.task_events] where job_id in
(select job_id from [google_cloud_data.task_events] where event_type = 1) AND event_type in (3,5,6) group by job_id limit 100

-- Jobs submitted and then evicted
select job_id, count(job_id) from [google_cloud_data.task_events] where job_id in
(select job_id from [google_cloud_data.task_events] where event_type = 0) AND event_type = 4 group by job_id limit 100

-- Canonical memory and Requested memory
select timestamp, canonical_mem, requested_memory from [google_cloud_data.task_events] JOIN [google_cloud_data.task_usage] ON [google_cloud_data.task_events.job_id] = [google_cloud_data.task_usage.job_id] limit 100
