import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';


const routes = {
  userComments: () => `/user/activities/comments/`,
  userStars: () => `/user/activities/stars/`
};


@Injectable()
export class UserActivitiesService {

  constructor(private httpClient: HttpClient) {
  }

  // todo creation date
  getComments(page: string = ''): Observable<any> {

    return this.httpClient
      .get(routes.userComments() + page, {withCredentials: true});

  }

  getStars(page: string = ''): Observable<any> {

    return this.httpClient
      .get(routes.userStars() + page, {withCredentials: true});

  }

}
