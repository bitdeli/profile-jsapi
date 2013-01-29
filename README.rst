
Javascript Library
------------------

This profile lets you access raw events from the Bitdeli :ref:`js-lib`.

- **Source:** A web site, via :ref:`js-api`

- **Historical data:** N/A

- **Retention:**
    - *Premium*: 365 days of events and inactive users.
    - *Advanced*: 365 days of events and inactive users.
    - *Basic*: 365 days of events and inactive users.

- **Schema:**
    .. code-block:: python

         {
             "$pageview": [
                [
                    timestamp,
                    group_key,
                    ip_address,
                    event
                ],
                ...
             "events": [
                [
                    timestamp,
                    group_key,
                    ip_address,
                    event
                ],
                ...
            ]
         }

    where *timestamp* is a server-side timestamp in UTC, *group_key* identifies the batch
    in which the event was processed, *ip_address* is the IP address of the sender,
    and *event* is the event object as defined in :ref:`js-api`.

- **Update interval:** 1 hour

- **Code:** `bitdeli/profile-jsapi <https://github.com/bitdeli/profile-jsapi>`_
