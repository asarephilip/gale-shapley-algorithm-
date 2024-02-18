"""
Implementation of the algorithm prioritizing the preferences of job seekers.

Prioritizing job seekers' proitity creates a user centric platform. When job seekers' are offered relevant opportunities,
it creates high user satisfaction which will increase engagement on the platform.
Prioritizing the job seekers' also indicate commitment to their interests.This can lead to high job-seeker retention rate.
"""


"""
job_seekers = [
    {"name": "Alice", "skills": ["Python Programming", "Project Management"]},
    {"name": "Bob", "skills": ["Python Programming"]},
    {"name": "Carol", "skills": ["Project Management"]},
    {"name": "Dave", "skills": []},
    {"name": "Eve", "skills": ["Python Programming", "Project Management"]}
]

job_openings = [
    {"company": "TechCorp", "required_skills": ["Python Programming"]},
    {"company": "BizCo", "required_skills": ["Project Management"]},
    {"company": "Innovatech", "required_skills": ["Python Programming", "Project Management"]},
    {"company": "AlphaTech", "required_skills": []},
    {"company": "OmegaSolutions", "required_skills": ["Python Programming"]}
]
This is the actual data structure given in the task. But I reduced it to a tuple of list containing skills of the job seekers.
This intention is to make the code simple as looping over dictionaries will make the code a little more complex.
Again, I could have done this in code, but since the focus is on the algorithm, I decided to focus on just that.

In the tuples below, the first list in the job_seeker tuple represent Alice's skills; the second maps to Bob; .... and the fifth maps to Eve. In that order.
The same order applies to te job_opening tuple.
"""

job_seekers = (
    ["Python Programming", "Project Management"],
    ["Python Programming"],
    ["Project Management"],
    [],
    ["Python Programming", "Project Management"]
)
job_openings = (
    ["Python Programming"],
    ["Project Management"],
    ["Python Programming", "Project Management"],
    [],
    ["Python Programming"]
)

# Job seekers who do not have any skills or may have skills that are not needed in any job opening.
unmatched_job_seekers = []
# Job openings which do not have any skills or may have skills that are not possessed by any job seeker.
unmatched_job_opening = []
# Job seekers who have been matched.
# Corresponding index in engaged_job_seekers and engaged_job_openings represents a job seeker that is matched to a job opening.
# For example, given engaged_job_seekers[0] and engaged_job_openings[0]. engaged_job_seekers[0] has been matched to the job opening at engaged_job_openings[0]
engaged_job_seekers = []
# Job openings that have been matched to a job seeker.
engaged_job_openings = []

# Index of job seekers. We would represent the job seekers by their index in the `job_seekers` tuple.
available_job_seekers = [i for i in range(len(job_seekers))]
# Index of job openings. We would represent the job openings by their index in the `job_openings` tuple.
available_job_openings = [i for i in range(len(job_openings))]

# Loop over the available job seekers and match them with a job opening prioritizing their skills.
while available_job_seekers:
    job_seeker_index = available_job_seekers.pop()  # The job seeker (the represented by an index)
    job_seeker_skills = job_seekers[job_seeker_index]  # The skills of the job seeker

    # If a job seeker has no skills, add him/her to the unmatched_job_seekers and continue with the next person.
    if not job_seeker_skills:
        unmatched_job_seekers.append(job_seeker_index)
        continue

    for job_seeker_skill in job_seeker_skills:
        #  For each skill possessed by the job seeker, check if there is a job opening that requires such skill.
        for job_opening_index, job_opening in enumerate(job_openings):
            #  If there is a job opening with such skill, and the job opening is unmatched, pair the job seeker with that job opening.
            #  At this point, we are pairing only based on availability, and not skill priority.
            if job_seeker_skill in job_opening:
                if job_seeker_index not in engaged_job_seekers and job_opening_index not in engaged_job_openings:
                    engaged_job_seekers.append(job_seeker_index)
                    engaged_job_openings.append(job_opening_index)
                    break
                # In the situation where the job seeker is already paired, we would like to ensure that the job seeker
                # is paired with his/her preferred job based on his/her skill priority.
                # If there is a job that better suits the job seeker's skills, we assign that job opening to the job seeker.
                elif job_seeker_index in engaged_job_seekers:
                    for job_opening_skill in job_opening:
                        if job_seeker_skills.index(job_seeker_skill) < job_opening.index(job_opening_skill):
                            previous_match_index = engaged_job_seekers.index(job_seeker_index)
                            engaged_job_openings[previous_match_index] = job_opening_index
                            break

unmatched_job_opening = set(available_job_openings).difference(engaged_job_openings)

# Pair up remaining job seekers and job openings
for job_seeker, job_opening in zip(unmatched_job_seekers, unmatched_job_opening):
    engaged_job_seekers.append(job_seeker)
    engaged_job_openings.append(job_opening)


# Pair up actual skill of matched job seekers and job openings and print them.
job_seeker_job_opening_pairs = []
for i, j in zip(engaged_job_seekers, engaged_job_openings):
    job_seeker_job_opening_pairs.append((job_seekers[i], job_openings[j]))
for pair in job_seeker_job_opening_pairs:
    print(pair)


def test_all_job_seekers_are_paired(available_job_seekers, engaged_job_seekers):
    assert not set(available_job_seekers).difference(engaged_job_seekers)


def test_all_job_openings_are_paired(available_job_openings, engaged_job_openings):
    assert not set(available_job_openings).difference(engaged_job_openings)


test_all_job_seekers_are_paired(available_job_seekers, engaged_job_seekers)
test_all_job_openings_are_paired(available_job_openings, engaged_job_openings)
