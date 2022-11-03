# -*- coding: utf-8 -*- #
# Copyright 2022 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""`gcloud service-directory registration-policies describe` command."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.service_directory import registration_policies
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.service_directory import resource_args

_RESOURCE_TYPE = 'registration_policy'


@base.ReleaseTracks(base.ReleaseTrack.ALPHA, base.ReleaseTrack.BETA)
class DescribeAlphaBeta(base.DescribeCommand):
  """Describe a registration policy."""

  detailed_help = {
      'EXAMPLES':
          """\
          To describe a Service Directory registration policy, run:

            $ {command} my-policy --location=my-location
          """,
  }

  @staticmethod
  def Args(parser):
    resource_args.AddRegistrationPolicyResourceArg(parser, 'to describe')

  def Run(self, args):
    client = registration_policies.RegistrationPoliciesClient()
    registration_policy_ref = args.CONCEPTS.registration_policy.Parse()

    return client.Describe(registration_policy_ref)
